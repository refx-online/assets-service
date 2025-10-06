build:
	docker build -t assets-service .

run:
	docker run --network=host --env-file=.env assets-service
