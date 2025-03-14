# Processing streams with quix streams

## Getting set up

```sudo quix pipeline up```

This gets kafka up and running. Fortunately, [quix](https://quix.io/get-started-with-quix-streams) obfuscates a lot of complexity here and this ends up being one simple command.

```python3 main.py```

We now begin producing events.

```kafkacat -b localhost:19092 -Ct github_events | jq .```

Use kafka to "consume topic" (`-Ct`) from the broker ('-b') on port `19092`.

Piping into `jq .` turns all formats Json events nicely.

## Closing things off

```Ctrl+C```

Execute this command in the tab where `main.py` was running to stop the events from showing.

```quix pipeline down```

Kills the docker container where kafka is running.

## Notes

```CDEBUG:requests_sse.client:close```
Shows that the process is being closed off properly:

[Quix application docs](https://quix.io/docs/quix-streams/api-reference/application.html#applicationconfigcopy)

## Troubleshooting

After running `sudo quix pipeline down`, If you are encountering the following error:

```bash
cannot stop container: <container ID>: permission denied
```

run `sudo aa-remove-unknown` and then run `sudo quix pipeline down` again.
