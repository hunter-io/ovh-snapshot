# Easily snapshot OVH instances using Docker

## Usage

First, create an API application on `https://eu.api.ovh.com/createApp/` and write down the provided `APPLICATION_KEY` AND `APPLICATION_SECRET`. You'll also need your `PROJECT_ID`.

Then, run the image once in interactive mode to request your consumer key:
```
docker run -it \
  -e ENDPOINT="YOUR_PUBLIC_CLOUD_ENDPOINT" \
  -e APPLICATION_KEY="THE_APPLICATION_KEY" \
  -e APPLICATION_SECRET="THE_APPLICATION_SECRET" \
  firmapi/ovh-snapshot python credentials.py
```

Follow the instructions, and write down the gotten `CONSUMER_KEY`.

You can now run the image again to list all the instances of your project:
```
docker run \
  -e ENDPOINT="YOUR_PUBLIC_CLOUD_ENDPOINT" \
  -e APPLICATION_KEY="THE_APPLICATION_KEY" \
  -e APPLICATION_SECRET="THE_APPLICATION_SECRET" \
  -e CONSUMER_KEY="THE_CONSUMER_KEY_FROM_PREVIOUS_STEP" \
  -e PROJECT_ID="YOUR_PROJECT_ID" \
  firmapi/ovh-snapshot python instances.py
```

This command will be useful to retrieve the identifiers of the instances you want to snapshot.

Finally, you can run the images without command to launch a snapshot of all the instances you provided:
```
docker run \
  -e ENDPOINT="YOUR_PUBLIC_CLOUD_ENDPOINT" \
  -e APPLICATION_KEY="THE_APPLICATION_KEY" \
  -e APPLICATION_SECRET="THE_APPLICATION_SECRET" \
  -e CONSUMER_KEY="THE_CONSUMER_KEY_FROM_PREVIOUS_STEP" \
  -e PROJECT_ID="YOUR_PROJECT_ID" \
  -e INSTANCES="COMMA_SEPARATED_LIST_OF_INSTANCE_TO_SNAPSHOT" \
  firmapi/ovh-snapshot
```
