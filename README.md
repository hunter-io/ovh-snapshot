# Easily snapshot OVH instances using Docker

## Configuration

Create an API application on `https://eu.api.ovh.com/createApp/` and write down the provided `APPLICATION_KEY` and `APPLICATION_SECRET`. You'll also need your `PROJECT_ID`.

Then, run the image in interactive mode to request your consumer key:
```
docker run -it \
  -e ENDPOINT="YOUR_PUBLIC_CLOUD_ENDPOINT" \
  -e APPLICATION_KEY="THE_APPLICATION_KEY" \
  -e APPLICATION_SECRET="THE_APPLICATION_SECRET" \
  quay.io/hunter-io/ovh-snapshot python credentials.py
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
  quay.io/hunter-io/ovh-snapshot python instances.py
```

This command is useful to retrieve the identifiers of the instances you want to snapshot.

## Usage

Once you got the `APPLICATION_KEY`, `APPLICATION_SECRET`, `CONSUMER_KEY` and `INSTANCES`, you can run the image without command to launch a snapshot of all the provided instances:
```
docker run \
  -e ENDPOINT="YOUR_PUBLIC_CLOUD_ENDPOINT" \
  -e APPLICATION_KEY="THE_APPLICATION_KEY" \
  -e APPLICATION_SECRET="THE_APPLICATION_SECRET" \
  -e CONSUMER_KEY="THE_CONSUMER_KEY_FROM_PREVIOUS_STEP" \
  -e PROJECT_ID="YOUR_PROJECT_ID" \
  -e INSTANCES="COMMA_SEPARATED_LIST_OF_INSTANCE_TO_SNAPSHOT" \
  quay.io/hunter-io/ovh-snapshot
```

You can also run the same image with the `python cleanup.py` command to keep only `NUMBER_SNAPSHOTS_TO_KEEP` per instance:
```
docker run \
  -e ENDPOINT="YOUR_PUBLIC_CLOUD_ENDPOINT" \
  -e APPLICATION_KEY="THE_APPLICATION_KEY" \
  -e APPLICATION_SECRET="THE_APPLICATION_SECRET" \
  -e CONSUMER_KEY="THE_CONSUMER_KEY_FROM_PREVIOUS_STEP" \
  -e PROJECT_ID="YOUR_PROJECT_ID" \
  -e INSTANCES="COMMA_SEPARATED_LIST_OF_INSTANCE_TO_SNAPSHOT" \
  -e NUMBER_SNAPSHOTS_TO_KEEP=4 (default: 3) \
  quay.io/hunter-io/ovh-snapshot python cleanup.py
```

## TODO

- [ ] Add Cronitor support
- [ ] Improve the error handling
