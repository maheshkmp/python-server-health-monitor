servers = {
    "web-01": {"cpu": 45, "memory": 62},
    "web-02": {"cpu": 82, "memory": 71},
    "db-01": {"cpu": 31, "memory": 88},
    "cache-01": {"cpu": 91, "memory": 93}
}

def check_servers(a):
	warnings = []
	for server, metrics in a.items():
		if metrics["cpu"]> 80 and metrics["memory"]> 80:
	 		warnings.append(f"{server}, cpu high, memory high")
		elif metrics["cpu"] > 80:
			warnings.append(f"{server}, cpu high")
		elif metrics["memory"]> 80:
			warnings.append(f"{server}, memory high")


	return warnings

results = check_servers(servers)
print(results)
