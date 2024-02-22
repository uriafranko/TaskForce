from load_dotenv import load_dotenv

from crews.template_crew.crew import TemplateCrew

load_dotenv()


def main():
    template_crew = TemplateCrew(example="I am an example")
    print(template_crew.description)
    print("Done!")


if __name__ == "__main__":
    main()
