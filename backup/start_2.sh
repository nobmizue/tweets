# backend PUBSUB to BQ
kubectl create -f pubsub/bigquery-controller.yaml
sleep 5
# frontend TWITTER to PUBSUB
kubectl create -f pubsub/twitter-stream.yaml
