# Color

Contains information on the colors used to describe items in the Harvard Art Museums collections.

## Get Colors

`GET /color` will get all colors.

Include one or more of the following parameters to filter the items.

| Parameter | Value |
| :--------- | :----- |
| apikey | YOUR API KEY required |
| q | FIELD:VALUE |
| size | 0-9+ |
| page | 0-9+ |
| sort | FIELD NAME or "random" or "random:[SEED NUMBER]" |
| sortorder | asc or desc |

#### Examples

> https://api.harvardartmuseums.org/color  
> Returns all of the colors. 

#### Response

```json
{
    "info": {
        "totalrecordsperquery": 3,
        "totalrecords": 147,
        "pages": 49,
        "page": 1
    },
    "records": [
        {
            "id": 34838386,
            "lastupdate": "2015-11-22T03:17:53-0500",
            "hex": "#f5f5dc",
            "name": "beige",
            "colorid": 34838386
        },
        {
            "id": 34838398,
            "lastupdate": "2015-11-22T03:17:53-0500",
            "hex": "#a52a2a",
            "name": "brown",
            "colorid": 34838398
        },
        {
            "id": 34838406,
            "lastupdate": "2015-11-22T03:17:53-0500",
            "hex": "#d2691e",
            "name": "chocolate",
            "colorid": 34838406
        }
    ]
}
```

## Get Color

`GET /color/COLOR_ID` will get the full record of the specified color.

#### Examples

> https://api.harvardartmuseums.org/color/34838406  
> Returns the full record for the color chocolate.  

#### Response

```json
{
    "colorid": 34838406,
    "name": "chocolate",
    "hex": "#d2691e",
    "id": 34838406,
    "lastupdate": "2015-11-22T03:17:53-0500"
}
```