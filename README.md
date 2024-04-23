# Cloud Basic - Final Assignment

The `Ruoppolo_report.pdf` contains all the details for deployment. Please refer to it. 

I paste the `Setup` section here.

## Setup

First of all the container has been created by a `.yml` file where two volumes have been specified, in our case two services: Nextcloud and a MariaDB database, with the corresponding \textbf{volumes} and networks. In particular for Nextcloud has been specified the localhost port 8080:80, so that the container can be accessible from the host OS. The servers has been linked through a network that enables the communication between the two.
Its execution has been made by simply running on the command line inside the directory containing the file the following command:

```
zsh docker compose up -d
```
that automatically creates the container based on the requested services, deploying the database and the Nextcloud filesystem, to which it is possible to access from the local machine by typing `https://localhost:8080` using admin username and password reported in the `.yml` file itself.
