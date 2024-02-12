from ddos_tool import ddos_tool

tools = {
    1: ddos_tool
}

print("""
  _____  _      _       _
 / ____|| |    (_)     | |
| (___  | |__   _  ___ | |__    ___
 \___ \ | '_ \ | |/ __|| '_ \  / _ \\
 ____) || | | || |\__ \| | | ||  __/
|_____/ |_| |_||_||___/|_| |_| \___|
""")
print("**** Hacking Tools ****\n")

print("Escolha a ferramente que você deseja usar:")
print("+------------+------------------+")
print("|DDoS Tool: 1| Lan Redirector: 2|")
print("+------------+------------------+")

tool = int(input())

tools[tool]()
