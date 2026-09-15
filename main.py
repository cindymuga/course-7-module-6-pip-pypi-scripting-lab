from datetime import datetime
import requests

def generate_log():
    today_str = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today_str}.txt"

    url = "https://jsonplaceholder.typicode.com/todos/1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        with open(filename, "w") as file:
            file.write(f"Automation Output Results:\n{data}\n")

        print(f"Successfully generated log: {filename}")
        return filename
    except Exception as e:
        print(f"Error generating log: {e}")
        return None

def main():
    generate_log()

if __name__ == "__main__":
    main()