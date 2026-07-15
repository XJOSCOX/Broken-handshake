Analyze the Apache-style access log at `/app/access.log` and write a JSON report to
`/app/report.json`.

1. The report is valid JSON.
2. The report contains `total_requests` with the total number of non-empty log lines.
3. The report contains `unique_clients` with the number of distinct client IPs.
4. The report contains `clients` as a sorted list of the distinct client IPs.
5. The report contains `path_counts`, an object mapping each requested path to its
   request count.
6. The report contains `top_path`, the most requested path. If there is a tie, choose
   the lexicographically smallest path among the tied paths.

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.
