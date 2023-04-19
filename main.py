import time
import argparse
import ping3
from uti import open_server_file, add_server_to_file, remove_server_in_file, add_checks_to_file, makelistchecks
from jinja2 import Environment, FileSystemLoader


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'mode', choices=['management', 'normal'], help='modes to choose from')
    args = parser.parse_args()

    if args.mode == 'management':
        print("test")
        ans = int(
            input("Would you like to: 1. add a server | 2. remove a server: "))
        if ans == 1:
            new_server = input(
                "Give the ip address of the server you like to add: ")
            print(add_server_to_file(new_server))
        if ans == 2:
            rm_server = input(
                "Give the ip address of the server you like to remove: ")
            print(remove_server_in_file(rm_server))
    elif args.mode == 'normal':
        servers = open_server_file()
        for server in servers:
            response_time = ping3.ping(server)
            if response_time != False:
                status = "online"
            else:
                status = "offline"
            add_checks_to_file(server, status, response_time)
            log_message = f"{server} is {status} (response time: {response_time})"
            print(log_message)

        checks = makelistchecks()
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('status_template.html')

        # Render the template with the server data
        html_output = template.render(servers=servers)

        # Write the HTML output to a file
        with open('status_template.html', 'w') as f:
            f.write(html_output)

#        time.sleep(10)  # wait for 60 seconds before pinging again


main()
