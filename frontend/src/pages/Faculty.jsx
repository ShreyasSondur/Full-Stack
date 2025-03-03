import React, { useEffect, useState } from "react"
import axios from 'axios'

function Faculty() {
  const endpoint = "http://127.0.0.1:8000/api/faculty"
  const [facultyData , setFacultyData] = useState([])
  //funcation to fetch
  const fetchData = async() =>{
    const response = await axios.get(endpoint)
    const {data} = response
    setFacultyData(data)
    return data
  }

  useEffect(() => {
    fetchData()
  }, [])
  

  return (
    <>
      <h1>Faculty Data</h1>
        {facultyData.map(el => 
        <div key={el.id}>
          <h1>{el.Name}</h1>
          <h1>{el.Phone}</h1>
        </div>
        )}
    </>
  )
}


export default Faculty
