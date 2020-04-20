# MongoDB en Docker

Los siguientes pasos para correr MongoDB en Docker Containers asume conocimiento 
basico de Docker y MongoDB.

Notas de este ejemplo:
* MongoDB corre en un Docker Container
* el container docker continuara corriendo en el background (opcion -d)
* el puerto usado por MongoDB se mantiene igual y se hace disponible al contenedor (opcion -p 27017:27017)
* los datos se mantienen en el computador local y no en el Container. Utilizando volumenes (opcion -v data:/data/db). Mongo guarda las colecciones en el directorio `/data/db`.  Esta opcion redirige los datos a un directorio local `data`
* el paso final es verificar que tenemos accesso a los datos utilizando el lenguaje Python

##### 1. Iniciar el servidor de MongoDB en Docker 

```shell

# Inicia MongoDB ultima version (latest) publicada
$ docker run -d -p 27017:27017 -v data:/data/db mongo
bf029f7c36c1....

# Permite confirmar que el container esta corriendo y tambien tenemos el ID 
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                      NAMES
bf029f7c36c1        mongo               "docker-entrypoint.s…"   1 week ago         Up 2 weeks          0.0.0.0:27017->27017/tcp   pedantic_jones

```

<details>
   <summary>ver pasos detallados..</summary>

```shell
# Inicia MongoDB ultima version (latest) publicada
$ docker run -d -p 27017:27017 -v data:/data/db mongo
bf029f7c36c1....

# Permite confirmar que el container esta corriendo y tambien tenemos el ID 
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                      NAMES
bf029f7c36c1        mongo               "docker-entrypoint.s…"   1 week ago         Up 2 weeks          0.0.0.0:27017->27017/tcp   pedantic_jones

# Inspeccionando el Container.  Informacion interesante del contenedor.
$ docker inspect bf029f7c36c1

$ docker inspect bf029f7c36c1
[
    {
        "Id": "bf029f7c36c1f7caaa84f7ccf989e9a37df16cf23786a84e5b5f6ec5fb495807",
        "Created": "2020-02-23T17:28:09.5524798Z",
        "Path": "docker-entrypoint.sh",
        "Args": [
            "mongod"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 4492,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2020-02-23T17:28:10.8336199Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:8e89dfef54ffe28ed865d61bee08d4fd6c29066f9955b30f500c9187515ebe6f",
        "ResolvConfPath": "/var/lib/docker/containers/bf029f7c36c1f7caaa84f7ccf989e9a37df16cf23786a84e5b5f6ec5fb495807/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/bf029f7c36c1f7caaa84f7ccf989e9a37df16cf23786a84e5b5f6ec5fb495807/hostname",
        "HostsPath": "/var/lib/docker/containers/bf029f7c36c1f7caaa84f7ccf989e9a37df16cf23786a84e5b5f6ec5fb495807/hosts",
        "LogPath": "/var/lib/docker/containers/bf029f7c36c1f7caaa84f7ccf989e9a37df16cf23786a84e5b5f6ec5fb495807/bf029f7c36c1f7caaa84f7ccf989e9a37df16cf23786a84e5b5f6ec5fb495807-json.log",
        "Name": "/flamboyant_leakey",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": [
                "data:/data/db"
            ],
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {
                "27017/tcp": [
                    {
                        "HostIp": "",
                        "HostPort": "27017"
                    }
                ]
            },
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "CapAdd": null,
            "CapDrop": null,
            "Capabilities": null,
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "ConsoleSize": [
                0,
                0
            ],
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": null,
            "BlkioDeviceWriteBps": null,
            "BlkioDeviceReadIOps": null,
            "BlkioDeviceWriteIOps": null,
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "KernelMemory": 0,
            "KernelMemoryTCP": 0,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": false,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/88f3baed5bc97fb2cea1bc4d3a32f890a757dbf6fafaf269b8c4c6965df43cdb-init/diff:/var/lib/docker/overlay2/b3b571422e1409b93e4619971d3bd0e256510644301991b4b02e35e09296d999/diff:/var/lib/docker/overlay2/c7932f746c83897455aa862aad6a899667ad60b805fcdc65a9e7360e25b065f6/diff:/var/lib/docker/overlay2/69f1bcecf447d3029bf320e301646cb58cc7b299abe27e0f274e86f20be32690/diff:/var/lib/docker/overlay2/9f7441d9560125c9e1af9f2d5afd372db8baf43cad9859d64486bf33a1ae2d3a/diff:/var/lib/docker/overlay2/6aa360287a7721b3379d5101965ffa858d5c6cf99a240332d15013ef2ca90f8e/diff:/var/lib/docker/overlay2/9f6347352997d43de1df71ea03131d713babe5c42aa7bd3703e11b4e01cbf5fe/diff:/var/lib/docker/overlay2/ae8b12e489ad570e9f7e1149184b892238d0ede23da64f077b1b26bbe36b0756/diff:/var/lib/docker/overlay2/c1caafe0ce126db82b7646c006b80dfc63b857ea4738ef04b7cf07d13fdffed2/diff:/var/lib/docker/overlay2/17b1224861a23349dd0f83b074c22134a169d88f81a529036557eeac04bdf5cb/diff:/var/lib/docker/overlay2/443cd64b5989f56a68cb377776d235f27b17174584c2493bcfcbaff691e4450a/diff:/var/lib/docker/overlay2/48acd3d8663d08126d14058e5a8395fb2fdd06e5dabf48cec9ab7eab3e6cd387/diff:/var/lib/docker/overlay2/1346a3d4860ed7fdcd2d016e90554fa7a6ea4996a543513c11cbd2b6a76e7ece/diff:/var/lib/docker/overlay2/2100cc18b821d64a83d4d5c78825f47561b1375b605750cf7cc04f447725b43d/diff",
                "MergedDir": "/var/lib/docker/overlay2/88f3baed5bc97fb2cea1bc4d3a32f890a757dbf6fafaf269b8c4c6965df43cdb/merged",
                "UpperDir": "/var/lib/docker/overlay2/88f3baed5bc97fb2cea1bc4d3a32f890a757dbf6fafaf269b8c4c6965df43cdb/diff",
                "WorkDir": "/var/lib/docker/overlay2/88f3baed5bc97fb2cea1bc4d3a32f890a757dbf6fafaf269b8c4c6965df43cdb/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [
            {
                "Type": "volume",
                "Name": "data",
                "Source": "/var/lib/docker/volumes/data/_data",
                "Destination": "/data/db",
                "Driver": "local",
                "Mode": "z",
                "RW": true,
                "Propagation": ""
            },
            {
                "Type": "volume",
                "Name": "05b0bb30b34052e20f67bda5633166a97c581e21392895aa5fb034b82a60d5ca",
                "Source": "/var/lib/docker/volumes/05b0bb30b34052e20f67bda5633166a97c581e21392895aa5fb034b82a60d5ca/_data",
                "Destination": "/data/configdb",
                "Driver": "local",
                "Mode": "",
                "RW": true,
                "Propagation": ""
            }
        ],
        "Config": {
            "Hostname": "bf029f7c36c1",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "27017/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "GOSU_VERSION=1.11",
                "JSYAML_VERSION=3.13.0",
                "GPG_KEYS=E162F504A20CDF15827F718D4B7C549A058F8B6B",
                "MONGO_PACKAGE=mongodb-org",
                "MONGO_REPO=repo.mongodb.org",
                "MONGO_MAJOR=4.2",
                "MONGO_VERSION=4.2.3"
            ],
            "Cmd": [
                "mongod"
            ],
            "Image": "mongo",
            "Volumes": {
                "/data/configdb": {},
                "/data/db": {}
            },
            "WorkingDir": "",
            "Entrypoint": [
                "docker-entrypoint.sh"
            ],
            "OnBuild": null,
            "Labels": {}
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "27fb994a7f1acab44e04ded066df0d46ad30bafc120b5ba1f7106fdb0b81845b",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "27017/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "27017"
                    }
                ]
            },
            "SandboxKey": "/var/run/docker/netns/27fb994a7f1a",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "f5464a4f1ed514e48ff15d7e985963b4c0249274ff71e7e6e5ff5e26b737f2e3",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:02",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "d0b1860dee597c25f08ab481aa6d3b0c644a991fcd880e0964f542d2b726d258",
                    "EndpointID": "f5464a4f1ed514e48ff15d7e985963b4c0249274ff71e7e6e5ff5e26b737f2e3",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:02",
                    "DriverOpts": null
                }
            }
        }
    }
]
```
</details>

##### 2. Verificar connectividad con Mongo

```shell
# utilizando el ID el comando anterior (docker ps) iniciamos una session the shell-bash 
# directamente en el container. El resultado es el cursor de "root" en el container
$ docker exec -it bf029f7c36c1 bash
root@bf029f7c36c1:/# 

# Inicial una session de Mongo CLI. El cursor ">" de MongoDB aparece al final
root@bf029f7c36c1:/# mongo 

MongoDB shell version v4.2.3
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("788c3d5c-d9b0-44ff-8249-cbc9997052d1") }
MongoDB server version: 4.2.3
.... <extra texto removido> ...
 
```


##### 3. En el cursor de MongoDB (>) verificar conectividad

Mas detalles de uso del Mongo CLI (shell) pueden verse en [manual de mongodb](https://docs.mongodb.com/manual/mongo/)

```
> show databases
admin   0.000GB
config  0.000GB
local   0.000GB
mydb    0.000GB

> use mydb
switched to db mydb

> show collections
cars
cities
post
recepies
```

##### 4. Salir del contendor

Para salir de MongoDB utilice CTRL-D o escriba ``exit``.  Luego, repita el mismo paso para salir del container.

```
> exit
bye
root@2d74364f4d16:/# exit
exit

# de regreso en el cursor del computador local
$ 
```


##### 5. Conectarse a la base de datos usando Python 3.x


En este paso se asume que ya tiene installado el paquete Python `PyMongo`.  

Para mas detalles en el uso del paquete utilice la referencia de W3School [PyMongo](https://www.w3schools.com/python/python_mongodb_getstarted.asp)

```shell
# en su computador personal teclee los siguientes comandos
$ python

Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

# En el shell de python
>>> from pymongo import MongoClient
>>> from pprint import pprint

# crear una conneccion a MongoDB (en el container)
>>> client = MongoClient('mongodb://localhost:27017/')

# crea y se conecta a la base de datos mydb
>>> db = client.mydb

# crea la coleccion cities
>>> collection = db.cities

# muestra el contenido de la variable collection
>>> pprint(collection)
Collection(Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), 'mydb'), 'cities')

# lista las colecciones disponibles (creadas por el usuario)
>>> pprint(db.list_collection_names())
['cities', 'post', 'cars']

# insertando un valor en la coleccion cities
>> a_city = {'name': 'Madrid', 'country': 'Spain'}
>> postid = collection.insert_one(a_city).inserted_id
>> print("inserted id: ", postid)
inserted id:  5e52f75a95e220e59383798c

# insertar otro documento en la coleccion. Sin pedir el _ID
>>> b_city = {'name': 'Madrid', 'country': 'Spain', 'languages':['Spanish','Catalan']}
>>> collection.insert_one(b_city)
<pymongo.results.InsertOneResult object at 0x110fedc88>

# lista contendio de la coleccion cities
>>> for a in collection.find():
...     print(a)
...
{'_id': ObjectId('5e3f3c3e6a2700f01d5ec888'), 'name': 'New York', 'country': 'USA'}
{'_id': ObjectId('5e3f3c3e6a2700f01d5ec889'), 'name': 'Paris', 'country': 'France'}
{'_id': ObjectId('5e3f5353b25a3628640a1e4c'), 'country': 'Canada', 'name': 'Vancouver'}
{'_id': ObjectId('5e3f5353b25a3628640a1e4d'), 'country': 'Mexico', 'name': 'Mexicali'}
{'_id': ObjectId('5e3f53eeb25a3628640a1e4e'), 'country': 'Canada', 'name': 'Quebec', 'languages': ['English', 'French']}
{'_id': ObjectId('5e45e8b09421f82f87eac0e8'), 'name': 'Los Angeles', 'country': 'USA'}
{'_id': ObjectId('5e51c9185bc8be528d159995'), 'name': 'Toronto', 'country': 'Canada'}
{'_id': ObjectId('5e52f75a95e220e59383798c'), 'name': 'Madrid', 'country': 'Spain'}
{'_id': ObjectId('5e52fe2495e220e59383798d'), 'name': 'Madrid', 'country': 'Spain', 'languages': ['Spanish', 'Catalan']}



```



##### 6. Acceso a MongoDB Container desde python (programa)

Este paso es bastante similar al #5 (arriba).  Ante todo, permite ilustrar un mini programa que se conecta y recupera documentos de la coleccion en MongoDB. 

Para correr el programa ejecute en la linea de comando `python test_pymongo.py`.  Luego, repita el mismo paso para salir del container.

```shell
$ python test_pymongo.py

# Resultados del programa
Collection(Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), 'mydb'), 'cities')

Colecciones disponibles
['recepies', 'cities', 'post', 'cars']

listado de coleccion: cities
{'_id': ObjectId('5e3f3c3e6a2700f01d5ec888'),
 'country': 'USA',
 'name': 'New York'}
{'_id': ObjectId('5e3f3c3e6a2700f01d5ec889'),
 'country': 'France',
 'name': 'Paris'}
{'_id': ObjectId('5e3f50f2b25a3628640a1e4b'),
 'country': 'USA',
 'name': 'Seattle'}
{'_id': ObjectId('5e3f5353b25a3628640a1e4c'),
 'country': 'Canada',
 'name': 'Vancouver'}
{'_id': ObjectId('5e3f5353b25a3628640a1e4d'),
 'country': 'Mexico',
 'name': 'Mexicali'}
{'_id': ObjectId('5e3f53eeb25a3628640a1e4e'),
 'country': 'Canada',
 'languages': ['English', 'French'],
 'name': 'Quebec'}
{'_id': ObjectId('5e45e8b09421f82f87eac0e8'),
 'country': 'USA',
 'name': 'Los Angeles'}
{'_id': ObjectId('5e51c9185bc8be528d159995'),
 'country': 'Canada',
 'name': 'Toronto'}
{'_id': ObjectId('5e52f75a95e220e59383798c'),
 'country': 'Spain',
 'name': 'Madrid'}
{'_id': ObjectId('5e52fe2495e220e59383798d'),
 'country': 'Spain',
 'languages': ['Spanish', 'Catalan'],
 'name': 'Madrid'}

Busca un documento. Si no existe, entonces lo inserta
Encontre..
{'_id': ObjectId('5e51c9185bc8be528d159995'),
 'country': 'Canada',
 'name': 'Toronto'}
 
 ```

