#### Create topics


```
docker exec -it kafka-0 kafka-topics \
  --bootstrap-server kafka-0:9092 \
  --command-config /etc/kafka/secrets/admin.properties \
  --create --topic topic-1 \
  --partitions 3 \
  --replication-factor 3
```

```
docker exec -it kafka-0 kafka-topics \
  --bootstrap-server kafka-0:9092 \
  --command-config /etc/kafka/secrets/admin.properties \
  --create --topic topic-2 \
  --partitions 3 \
  --replication-factor 3
```

### Settings ACL
 - Producer rights to record in the topic-1

```
docker exec -it kafka-0 kafka-acls \
  --bootstrap-server kafka-0:9092 \
  --command-config /etc/kafka/secrets/admin.properties \
  --add \
  --allow-principal User:producer \
  --operation Write \
  --topic topic-1
```

 - Consumer rights to read in the topic-1

 ```
 docker exec -it kafka-0 kafka-acls \
  --bootstrap-server kafka-0:9092 \
  --command-config /etc/kafka/secrets/admin.properties \
  --add \
  --allow-principal User:consumer \
  --operation Read \
  --topic topic-1 \
  --group consumer-ssl-group
```


 - Producer rights to record in the topic-2
 ```
docker exec -it kafka-0 kafka-acls \
  --bootstrap-server kafka-0:9092 \
  --command-config /etc/kafka/secrets/admin.properties \
  --add \
  --allow-principal User:producer \
  --operation Write \
  --topic topic-2
```


