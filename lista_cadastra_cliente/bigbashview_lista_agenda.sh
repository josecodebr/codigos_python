#!/bin/bash

# Nome do arquivo JSON
json_file="agenda.json"

# Início da tabela HTML e cabeçalho
echo "<!DOCTYPE html>
<html lang=\"pt-BR\">
    <head>
        <meta charset=\"UTF-8\">
        <title>Tabela de Agendas</title>
        <!--<link rel='stylesheet' href='styles.css'>-->
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
                }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                    }
            th {
                background-color: #ffaa7f;
                }
            td{
                background-color: #8ca18b;
            }
            
            .cabecario {
                background-color: #57e6fc;
                color: #1a1629;
                padding: 2px;
                margin: 10px;
                border: 1px solid #dddddd;
                border-radius: 5px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                flex: 1;
                
            }
        </style>
    </head>
    <body>
        <h1>Lista de CLientes</h1>
    <table id=\"planilha\">
        <tr>
            <th>Data</th><th>Manhã</th><th>Tarde</th><th>Noite</th>
        </tr>"
        # Loop para ler cada linha do arquivo JSON e formatar como linha da tabela HTML
        while IFS= read -r line; do
            # Extrair valores de manha, idade e email usando awk
            data=$(echo "$line" | awk -F'"data": ' '{print $2}' | cut -d'"' -f2)
            manha=$(echo "$line" | awk -F'"manha": ' '{print $2}' | cut -d'"' -f2)
            tarde=$(echo "$line" | awk -F'"tarde": ' '{print $2}' | cut -d'"' -f2)
            noite=$(echo "$line" | awk -F'"noite": ' '{print $2}' | cut -d'"' -f2)
            
            # Imprimir linha da tabela HTML
            echo " <tr>
                        <td>$data</td><td>$manha</td><td>$tarde</td><td>$noite</td>
                    </tr>"
        done < "$json_file"

    echo "</table>

    </body>
    </html>"
