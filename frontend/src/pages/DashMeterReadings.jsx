import { useState, useEffect } from 'react'
import api from '../api'

export default function DashMeterReadings() {
  const [meterReadings, setMeterReadings] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  useEffect(() => {
    const fetchMeterReadings = async () => {
      try {
        setLoading(true)
        const response = await api.get('/meter-readings')
        setMeterReadings(response.data)
        setLoading(false)
      } catch (error) {
        setError(error)
      }
    }
    fetchMeterReadings()
    }, []
  )

  if (loading) return <div>Loading...</div>
  if (error) return <div>{error.message}</div>
  console.log(meterReadings)

  return (
    <div>
      <h1 className='font-bold text-2xl'>Meter Readings</h1>
      <hr />
      <div className='grid grid-cols-4 gap-4'>
        {meterReadings.map((meterReading, index) => (
          <div key={index} className="max-w-sm rounded overflow-hidden shadow-lg">
            <img className="w-full" src={`http://localhost:7000/api/v1/meter-readings/uploads/`+meterReading.reading_image} alt="Meter Reading Image"></img>
            <div className="px-6 py-4">
              <div className="font-bold text-xl mb-2">{meterReading.reading}</div>
              <p className="text-gray-700 text-base">
                {meterReading.comments}
              </p>
            </div>
            <div className="px-6 pt-4 pb-2">
              <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">{meterReading.reading_date}</span>
              <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">Meter id:{meterReading.meter_id}</span>
              {/* <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#{meterReading.meterReading_type}</span> */}
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
