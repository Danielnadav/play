pipeline {
    agent any

    stages {

        stage ('Running C* Backup') {
            agent any

            steps {
                echo 'Running c* Backup, '

                sh '''

                    set -e"
                    _BACKUP_DIR=/tmp/backup"
                    _DATA_DIR=/var/lib/cassandra/data"
                    _NODETOOL=$(which nodetool)"
                    _TODAY_TIME=$(date +"%H.%M")"
                    _TODAY_DATE=$(date +%F)"
                    _BACKUP_SNAPSHOT_DIR="$_BACKUP_DIR/$_TODAY_DATE/$_TODAY_TIME"
                    _BACKUP_SCHEMA_DIR="$_BACKUP_DIR/$_TODAY_DATE/SCHEMA"
                    _SNAPSHOT_DIR=$(find $_DATA_DIR -type d -name snapshots)"
                    _SNAPSHOT_NAME=$(date +%F-%H%M-%S)"
                    _DATE_SCHEMA=$(date +%F-%H%M-%S)"
                    if [ -d  "$_BACKUP_SCHEMA_DIR" ]
                    then
                        echo "$_BACKUP_SCHEMA_DIR already exist"
                    else
                        mkdir -p "$_BACKUP_SCHEMA_DIR"
                    fi

                    if [ -d  "$_BACKUP_SNAPSHOT_DIR" ]
                    then
                        echo "$_BACKUP_SNAPSHOT_DIR already exist"
                    else
                        mkdir -p "$_BACKUP_SNAPSHOT_DIR"
                    fi
                    ##################### SECTION 1 : SCHEMA BACKUP ############################################

                    ## List All Keyspaces
                    cqlsh -e "DESC KEYSPACES" |perl -pe 's/\e([^\[\]]|\[.*?[a-zA-Z]|\].*?\a)//g' | sed '/^$/d' > Keyspace_name_schema.cql

                    #_KEYSPACE_NAME=$(cat Keyspace_name_schema.cql)

                    ## Create directory inside backup SCHEMA directory. As per keyspace name.
                    for i in $(cat Keyspace_name_schema.cql)
                    do
                        if [ -d $i ]
                        then
                            echo "$i directory exist"
                        else
                            mkdir -p $_BACKUP_SCHEMA_DIR/$i
                        fi
                    done

                    ## Take SCHEMA Backup - All Keyspace and All tables
                    for VAR_KEYSPACE in $(cat Keyspace_name_schema.cql)
                    do
                        cqlsh -e "DESC KEYSPACE  $VAR_KEYSPACE" > "$_BACKUP_SCHEMA_DIR/$VAR_KEYSPACE/$VAR_KEYSPACE"_schema-"$_DATE_SCHEMA".cql
                    done


                    ##################### END OF LINE ---- SECTION 1 : SCHEMA BACKUP #####################

                    ###### Create snapshots for all keyspaces
                    echo "creating snapshots for "Jaco" keyspace ....."

                    _NODETOOL snapshot jaco -t $_SNAPSHOT_NAME

                    ###### Get Snapshot directory path
                    _SNAPSHOT_DIR_LIST=`find $_DATA_DIR -type d -name snapshots|awk '{gsub("'$_DATA_DIR'", "");print}' > snapshot_dir_list`

                    #echo $_SNAPSHOT_DIR_LIST > snapshot_dir_list

                    ## Create directory inside backup directory. As per keyspace name.
                    for i in `cat snapshot_dir_list`
                    do
                        if [ -d $_BACKUP_SNAPSHOT_DIR/$i ]
                        then
                            echo "$i directory exist"
                        else
                            mkdir -p $_BACKUP_SNAPSHOT_DIR/$i
                            echo $i Directory is created
                        fi
                    done

                    ### Copy default Snapshot dir to backup dir

                    find $_DATA_DIR -type d -name $_SNAPSHOT_NAME > snp_dir_list

                    for SNP_VAR in `cat snp_dir_list`;
                    do
                        ## Triming _DATA_DIR
                        _SNP_PATH_TRIM=`echo $SNP_VAR|awk '{gsub("'$_DATA_DIR'", "");print}'`

                        cp -prvf "$SNP_VAR" "$_BACKUP_SNAPSHOT_DIR$_SNP_PATH_TRIM";
                        sudo aws s3 cp $_BACKUP_DIR s3://cassandrabackups1 --recursive

                    done 

                '''
            }
        }
    }
}