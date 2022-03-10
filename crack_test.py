from task_two import PasswordTool


def main():
    tool = PasswordTool("test-input")
    tool.words_list = ["imagine"]
    tool.run()

if __name__ == "__main__":
    main()