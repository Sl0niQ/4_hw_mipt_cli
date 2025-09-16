#file manager
import argparse
import cli_lib

def main():
    """
        file manager for CLI
        removes file 
        removes folder
        copies file
        analyzes folder
    """
    #parser object to get args from the cli
    parser = argparse.ArgumentParser(
                     prog = "file manager",
                     description = "allows you to perform some actions with a file or folder",
                     epilog = "examples:\n manager copy -o <file_name>"
    )

    #manager arguments declaring
    parser.add_argument("action", type = str, help = "allowed action")
    parser.add_argument("--origin", "-o", type = str, default = "", help = "original file name or path")
    parser.add_argument("--target", "-t", type = str, default = "", help = "target file name or path")

    args = parser.parse_args()

    #valid function call
    if args.action in cli_lib.actions:
        #print(args) 
        cli_lib.actions[args.action](args)  
    else:
        print("error: unknown argument <action>")

if __name__ == "__main__":
    main()