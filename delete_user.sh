#!/bin/bash

# Nome del container Docker di Nextcloud
NEXTCLOUD_CONTAINER_NAME="cloud-app-1"

for i in {81..180}
do
    # Costruisce lo username
    USERNAME="locust_user${i}"

    # Esegue il comando occ all'interno del container Docker per rimuovere l'utente
    docker exec --user www-data $NEXTCLOUD_CONTAINER_NAME /var/www/html/occ user:delete "$USERNAME"
    
    echo "Utente $USERNAME rimosso"
done

echo "Processo di rimozione degli utenti completato."

