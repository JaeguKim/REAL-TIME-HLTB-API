# HowLongToBeat-Crawling-Server   
This is python django server crawling howlongtobeat.com.

## How To Run Server
```python manage.py runserver``` in ```/HLTB_API' directory```

## API
### Show length of given video-game
----
  Returns json data about a given game title.

* **URL**

  /hltb/:title

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `title=[string]`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:**   
    `{
    "results": "Success",   
    "The Last of Us Part II": {   
        "completionist": 38.5,   
        "main": 23,   
        "main+extra": 28.5   
    },   
    "The Last of Us Remastered": {   
        "completionist": 27,   
        "main": 14.5,   
        "main+extra": 17   
    },   
    "The Last of Us": {   
        "completionist": 22,   
        "main": 15.5,   
        "main+extra": 17.5   
    },   
    "The Last of Us Left Behind": {   
        "completionist": 3,   
        "main": 2.5,   
        "main+extra": 2.5   
    }   
}`
 
* **Error Response:**

  * **Code:** 500 NOT FOUND <br />
    **Content:** `{ error : "Title doesn't exist" }`

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/hltb/last of us",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
