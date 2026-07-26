# AI Prompt Toolkit
# Version 1

prompts = {}

while True:
    print("\n===== AI Prompt Toolkit =====")
    print("1. Add Prompt")
    print("2. View Prompts")
    print("3. Search Prompt")
    print("4. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        category = input("Enter category: ")
        prompt = input("Enter your AI prompt: ")

        if category not in prompts:
            prompts[category] = []

        prompts[category].append(prompt)

        print("Prompt saved successfully!")

    elif choice == "2":
        if not prompts:
            print("No prompts saved yet.")
        else:
            print("\nSaved Prompts:\n")
            for category, items in prompts.items():
                print(f"[{category}]")
                for i, item in enumerate(items, start=1):
                    print(f"  {i}. {item}")
                print()

    elif choice == "3":
        keyword = input("Enter a keyword to search: ").lower()

        found = False

        for category, items in prompts.items():
            for item in items:
                if keyword in item.lower():
                    print(f"\nCategory: {category}")
                    print(f"Prompt: {item}\n")
                    found = True

        if not found:
            print("No matching prompts found.")

    elif choice == "4":
        print("Thank you for using AI Prompt Toolkit!")
        break

    else:
        print("Invalid choice. Please try again.")
