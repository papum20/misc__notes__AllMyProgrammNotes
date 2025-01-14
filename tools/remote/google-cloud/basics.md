# BASICS

## Configuration

set `Private Google Access` to `On`, for `default` subnet in the zone you're going to use (e.g.: `west-central1`) for `default` VPC network.  

Use default network, which has firewall rule `default-allow-internal` enabled.  


## Refs

tutorial for `spark` and `scala` on google-cloud: `https://cloud.google.com/dataproc/docs/tutorials/spark-scala`  


## Troubleshooting

When creating dataproc buckets, with `gcloud`, use `--uniform-bucket-level-access` : otherwise there are problems with ACLs, unless specific permissions for the default user are enabled.  

Possible APIs to enable for your project :
*	`dataproc API` : 
*	`Cloud Resource Manager API` : 

