import pulumi
import pulumi_eks as eks

project_name = pulumi.get_project()

# Create an EKS cluster with the default configuration.
cluster = eks.Cluster(
    f"{project_name}-1",
    instance_type="t3.micro",
    desired_capacity=2,
    min_size=2,
    max_size=2,
)

# Export the cluster's kubeconfig.
pulumi.export("kubeconfig", cluster.kubeconfig)
