
#### Scaled up version of master

- In total run as  5 services
- 3 app services(node1,node2,node3) scaled into 3,2,1 containers each
- nginx load-balancer service
- database service (persistency needs testing )

```
<!-- how to run -->
docker-compose up --build --remove-orphans -d  --scale node1=3 --scale node2=2
```
