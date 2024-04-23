#!/bin/bash

# Nome del container Docker di Nextcloud
NEXTCLOUD_CONTAINER_NAME="cloud-app-1"

for i in {0..89}
do
    # Costruisce lo username
    USERNAME="locust_user${i}"

    # Esegue il comando occ all'interno del container Docker per rimuovere i file dello storage dell'utente
    # Nota: la directory dell'utente deve essere specificata correttamente
    docker exec --user www-data $NEXTCLOUD_CONTAINER_NAME sh -c "rm -rf /var/www/html/data/$USERNAME/files/*"

    # Esegue il comando occ per ripulire eventuali dati residui nella cache dei file
    docker exec --user www-data $NEXTCLOUD_CONTAINER_NAME /var/www/html/occ files:scan --path="$USERNAME/files"

    echo "Storage dell'utente $USERNAME ripulito."
done

echo "Processo di pulizia degli storage degli utenti completato."
