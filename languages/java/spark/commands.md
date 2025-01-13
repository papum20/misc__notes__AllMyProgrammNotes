# COMMANDS

## Run

`spark-shell` : interactive shell  
`pyspark` : interactive, python  

## Start

`start-all.sh` : start both master and worker instances  

`start-master.sh` : start master node  
*	`http://127.0.0.1:8080/` : web UI

`start-worker [-c CORES] [-m MEM] spark://MASTER-IP:7077` : start worker 
*	do after `start-master`
*	`CORES` : number of cores to use (default all)
*	`MEM` : memory to use (default all)
	*	e.g.: `512M`

## Stop

`stop-all.sh` : stop both  
`stop-worker.sh` : stop one worker  
`stop-master.sh` : stop master  



