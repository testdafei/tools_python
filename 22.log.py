import subprocess
cmd = ['osascript', '-e', 'tell app "Finder" to activate']
result = subprocess.run(cmd, capture_output=True, text=True)
print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)