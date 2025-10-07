import sys

if len(sys.argv) < 2:
    print("⚠️ No name provided!")
else:
    name = sys.argv[1]
    print(f"👋 Hello {name} from composite Python action! 🚀")

