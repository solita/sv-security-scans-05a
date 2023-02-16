import subprocess


def command_execution_unsafe(request):
    if request.method == 'POST':
        action = request.POST.get('action', '')
        #BAD -- No sanitizing of input
        subprocess.call(["application", action])
