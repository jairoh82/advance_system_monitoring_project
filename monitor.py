# System Monitoring Project
# Demonstrates system checks, user input, and troubleshooting logic

def check_system(temp, volt, status):
    issues = []

    if temp > 90:
        issues.append("High temperature detected - inspect cooling system")

    if volt < 12.0:
        issues.append("Low voltage detected - check power supply or connections")

    if status.lower() != "ok":
        issues.append("System fault detected - inspect components and signals")

    return issues


def main():
    print("=== System Monitor ===")

    try:
        temperature = float(input("Enter system temperature: "))
        voltage = float(input("Enter system voltage: "))
        system_status = input("Enter system status (OK/FAULT): ")

        issues = check_system(temperature, voltage, system_status)

        print("\n--- System Report ---")

        if issues:
            print("ALERTS:")
            for issue in issues:
                print(f"- {issue}")
        else:
            print("System running normally")

    except ValueError:
        print("Invalid input - please enter correct values")


if __name__ == "__main__":
    main()