import React, { useEffect, useState } from "react"
import axios from 'axios'

function Dep() {
  const endpoint = "http://127.0.0.1:8000/api/department"
  const [DepData , setDepData] = useState([])
  //funcation to fetch
  const fetchData = async() =>{
    const response = await axios.get(endpoint)
    const {data} = response
    setDepData(data)
    return data
  }

  useEffect(() => {
    fetchData()
  }, [])
  

  return (
    <>
      <h2>Dep Data</h2>
        {DepData.map(el => 
        <div key={el.id}>
          <h1>{el.Name}</h1>
          <h1>{el.HOD}</h1>
        </div>
        )}
    </>
  )
}


export default Dep
