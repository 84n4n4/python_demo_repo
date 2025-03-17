from pydantic_settings_demo.demo_config import config

def main():
    print(config.DB_HOST)

if __name__ == "__main__":
    main()