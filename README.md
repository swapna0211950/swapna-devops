# swapna-devops

3-tier environment setup on GCP.

this setup involves.

1. Wordpress site installed on GKE
2. Network and LB
3. SQL DB

Terraform code does the below.

1. Creates VPC network, subnet for App and DB each.
2. Creates GKE cluster to deploy App.
3. Create a service to expose the APP using LB.
4. Create sql instance.
5. VPC peering between APP and DB VPC's.

Incoming requests comes through Exposed LB --> Workpress site(GKE cluster) --> DB
