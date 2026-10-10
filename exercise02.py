import json

def load_server(filename):
	try:
		with open(filename, "r") as file:
			servers = json.load(file)
		return servers

	except  FileNotFoundError:
		print("ERROR: Server file not found")

	except  json.JSONDecodeError:
		print("ERROR: Invalid JSON format")
		


def check_server(servers):
	warnings = []
	for server, metrics in  servers.items():
		if metrics["cpu"] > 80 and metrics["memory"]> 80:
			warnings.append(f"{server} - high cpu & high memory")
			
		elif metrics["cpu"] > 80:
			warnings.append(f"{server} - high cpu")
                        

		elif metrics["memory"] > 80:
			warnings.append(f"{server} - high memory")
                        

	
	return warnings

servers = load_server("servers.json")

if servers is not None:

	results = check_server(servers)
	print("Checking server health...\n")

	if len(results) > 0:
		for warning in results:
			print(warning)
		print(f"\nTotal warnings = {len(results)}")
	else:
		print("All servers are healthy")

