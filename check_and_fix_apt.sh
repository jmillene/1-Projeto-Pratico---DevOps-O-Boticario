#!/bin/bash

# Verifica se o script de pós-invocação do APT existe
if [ -f "/etc/apt/apt.conf.d/99update-not-found" ]; then
    # Remove o script de pós-invocação do APT
    sudo rm /etc/apt/apt.conf.d/99update-not-found
    echo "Script de pós-invocação do APT removido."
else
    # Se o script não existir, instala o command-not-found
    sudo apt-get install --reinstall command-not-found
    echo "command-not-found instalado."
fi

# Reinstala todos os pacotes do sistema
sudo apt-get install --reinstall $(dpkg -l | grep ^ii | awk '{print $2}')
echo "Reinstalação de todos os pacotes concluída."

# Atualiza o APT
sudo apt-get update
echo "APT atualizado."
