# 4_BDI_25mar_Cloud_Activity

Usefull commands:

    Build image:
        - docker build . -t <container_name>
    Run container with volume:
        - docker run -it -v $(pwd)/source:/root/source_container <container_name>
    Run container with volume using python command which executes the code: ( Comment the postgresSQL lines in script.py, if you don't have the postgres container running )
        - docker run -it -v $(pwd)/source:/root/source_container <container_name> python /root/source_container/script.py
    Run compose:
        - docker-compose up
    Run compose in background:
        - docker-compose up -d
