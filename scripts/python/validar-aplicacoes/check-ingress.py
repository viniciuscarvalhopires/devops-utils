import json
from termcolor import colored
import os, subprocess, argparse, traceback
from kubernetes import client, config

parser = argparse.ArgumentParser(description='Check ingress')
parser.add_argument('--path', help='Diretório kubeconfig', required=False)
args = parser.parse_args()

if args.path:
    kubeconfig_folder = args.path
else:
    kubeconfig_folder = os.path.expanduser('~') + '/.kube/'

files = os.listdir( kubeconfig_folder )

for file in files:
    try:
        kubeconfig_path = kubeconfig_folder + file
        print( colored( 'Checking ' + file, 'yellow', attrs=['bold', 'underline'] ) )
        config.load_kube_config( kubeconfig_path )
        core_api = client.CoreV1Api()
        networking_api = client.NetworkingV1Api()
        namespaces = core_api.list_namespace().items
        for namespace in namespaces:
            
            print (namespace.metadata.name)
            ingress = networking_api.list_namespaced_ingress( namespace.metadata.name ).items
            for item in ingress:
                data = client.ApiClient().sanitize_for_serialization(item)
                service_name = data['spec']['rules'][0]['http']['paths'][0]['backend']['service']['name']
                print( colored( '='*60, 'magenta' ) )
                print( colored( 'Namespace: ' + namespace.metadata.name, 'white' ) )
                print( colored( 'Ingress: ' + item.metadata.name, 'green' ) )
                print( colored( 'Hosts: ' + str( item.spec.rules[0].host ), 'cyan', attrs=['bold'] ) )
                print( colored('Service: ' + service_name, 'green'))
                curl = 'curl -s -o /dev/null -w "%{http_code}" ' + str(item.spec.rules[0].host)
                try:
                    http_status_code = subprocess.check_output(curl, shell=True)
                    http_status_code = http_status_code.decode().strip()  # Converte bytes para string                        
                    # Atribui a cor com base no código HTTP
                    text = f"HTTP Status code: {http_status_code}"
                    if http_status_code.startswith('2'):
                        text = f"HTTP Status code: {http_status_code} OK"
                        color = 'green'
                    elif http_status_code.startswith('3'):
                        text = f"HTTP Status code: {http_status_code} REDIRECT"
                        color = 'yellow'
                    else:
                        
                        color = "red"
                    
                    colored_http_status = colored(text, color, attrs=['bold'])
                    print(colored_http_status)

                except subprocess.CalledProcessError as e:
                    print(colored(f"Erro ao executar o comando curl: {e.returncode}", "red"))
                continue

    except Exception as e:
        print( colored(f"Erro ao conectar-se ao cluster usando o arquivo {file}: {str(e)}", "red"))

    print( colored( '='*120, 'blue' ) )
    print( colored( '='*120, 'blue' ) )
    continue
    