import os
import subprocess
from argparse import ArgumentParser
from argparse import Namespace

from msu.csc232.exceptions.grading_exceptions import MethodError


def get_parameters() -> Namespace:
    """
    Obtain script command-line arguments.
    :return: Namespace encapsulating this scripts command-line arguments
    """
    parser = ArgumentParser()
    parser.add_argument('-c', '--category', type=str, default='lab', help='The assignment category to grade, e.g., lab')
    parser.add_argument('-n', '--number', type=str, default='01', help='The assignment number, e.g., 01, 02, etc.')
    parser.add_argument('-u', '--username', type=str, help='GitHub username')
    parser.add_argument('-t', '--title', type=str, default='', help='Title of the assignment')
    parser.add_argument('-m', '--method', type=str, default='ssh', help='Cloning method, e.g., ssh or https')

    return parser.parse_args()


def get_repo_url(args: Namespace) -> str:
    """
    Extract the assignment repository url from the given Namespace.
    :rtype: object
    :param args: a Namespace containing parsed command-line arguments
    :return: The assignment repository url is returned.
    """
    category = args.category()
    number = args.number()
    username = args.username()
    title = args.title()
    method = args.method()
    repo = f'{category}{number}-{title}-{username}.git'

    if method == 'https':
        url = f'{method}://github.com/msu-csc232-sp20/{repo}'
    elif method == 'ssh':
        url = f'git@github.com:msu-csc232-sp20/{repo}'
    else:
        raise MethodError(method, 'Invalid method for cloning a repo was given.')
    return url


def main() -> None:
    """
    Entry point of this script.
    :return: None.
    """
    try:
        args = get_parameters()
        category = args.category
        number = args.number
        username = args.username
        title = args.title
        method = args.method
        repo = f'{category}{number}-{title}-{username}.git'

        if method == 'https':
            url = f'{method}://github.com/msu-csc232-sp20/{repo}'
        elif method == 'ssh':
            url = f'git@github.com:msu-csc232-sp20/{repo}'
        else:
            raise MethodError(method, 'Invalid method for cloning a repo was given.')

        print(f'Attempting to clone {url} ...')
        p = subprocess.run(["git", "clone", url], capture_output=True, check=True)
        if p.returncode == 128:
            problem = p.stderr.decode('utf-8')
            if "ERROR" in problem:
                print('Repo apparently doesn\'t exist')
            elif "destination" in problem:
                print('Repo already cloned...')
            else:
                print(f'Something went wrong in attempting to clone {url}')
            raise ChildProcessError
        print('Success!')

        cwd = os.path.dirname(os.path.realpath(__file__))
        mf = f'{cwd}/{url}'[len(cwd + 'git@github.com:msu-csc232-sp20/') + 1:-4]
        repo_dir = f'{cwd}/{mf}'
        grade_assignment_commands = f'''
        cd {repo_dir}
        echo "\n\n------ Checking out develop branch ------\n"
        git checkout develop
        echo "\n\n------ Commit Messages ------\n"
        git log
        echo "\n\n------ Building Test Target ------\n"
        mkdir build
        cd build
        export CXXFLAGS='-std=c++11'
        cmake -G "Unix Makefiles" ..
        make
        echo "\n\n------ Running Test Target ------\n"
        ./{category}{number}Test
        cd ../..
        '''
        p = subprocess.run([f'{grade_assignment_commands}'], shell=True, capture_output=True)
        results = p.stdout.decode('utf-8')
        print(results)

        with open(f'results-{category}{number}-{username}.txt', 'w') as f:
            f.write(results)

        push_results_commands = f'''
        pwd
        ls
        cp ./results-{category}{number}-{username}.txt {repo_dir}
        cd {repo_dir}
        pwd
        ls
        git add .
        git commit -am"Import grade results."
        git push
        cd ..
        '''
        p = subprocess.run([f'{push_results_commands}'], shell=True, capture_output=True)
        results = p.stdout.decode('utf-8')
        print(results)
    except MethodError as e:
        print(e.message)
        raise e
    except ChildProcessError as cpe:
        print('Child process error was caught')
        raise cpe


if __name__ == '__main__':
    main()
