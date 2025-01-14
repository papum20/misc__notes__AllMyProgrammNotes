# BASICS

## Web UI

You can monitor jobs, or see past jobs, from the Spark Web UI
*	src: `https://spark.apache.org/docs/3.5.0/web-ui.html`

### History server

Enabling it :
*	you should probably follow these steps:
	*	create `$SPARK_HOME/conf/spark-defaults.conf`, possibly from the provided template `$SPARK_HOME/conf/spark-defaults.conf.template`
	*	these should be the critical lines, to enable logging for spark so that the history server can use them :
		*	```
			spark.master                     spark://master:7077
			spark.eventLog.enabled           true
			# log dir of your choice
			spark.eventLog.dir               file:///tmp/spark-events
			# this compresses logs
			spark.eventLog.compress          true
			```
	*	src: https://www.ibm.com/docs/en/pasc/1.1.1?topic=ego-enabling-spark-history-service
*	the logs directory should be already existing
	*	so first create it (by default, it's `/tmp/spark-events`)
	*	or `start-history-server.sh` (and other `spark` commands) will complain about it


## Links

`http://127.0.0.1:8080/` : master standalone Web UI  
`http://127.0.0.1:7070/` : master  
`http://127.0.0.1:4040/` : currently running jobs  
*	you can see monitor them

`http://127.0.0.1:18080/` : history server  
*	you can see past jobs here


