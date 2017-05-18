# LC_Reply_Times
Calculates reply times for /r/livecounting and posts results

## How to Use

1. Download Python using Anaconda Distrubiton
2. Download the files into a directory
3. Run collect.py in directory
4. Enter Start and End IDs. Read How to Find IDs if you cannot locate IDs
5. The reply times calculations will be in stats.txt

## How to find IDs

1. Permalink a starting update
2. Copy the URL, it will look something like this: https://www.reddit.com/live/ta535s1hq2je/updates/a617b6f6-3bde-11e7-9354-0ef691894178
3. The last part of the URL, a617b6f6-3bde-11e7-9354-0ef691894178, is the ID

## Stats.txt looks wrong or is missing data

Possible Errors:

1. You have forgotten to include a start or end ID or mistyped it
2. You have selected a range that is less or more than 1000 counts
3. You have selected a range in which the reply times are too long (ex. longer than an hour)
4. You have selected a range in which there are multiple missing or duplicate counts

If none of these errors apply to you, than I'm currently in the process of fixing the error (hopefully)
