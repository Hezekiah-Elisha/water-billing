import React from 'react'
import api from '../api'

export default function DashMeters() {
  const [meters, setMeters] = React.useState([])
  const [loading, setLoading] = React.useState(false)
  const [error, setError] = React.useState(null)

  React.useEffect(() => {
    const fetchMeters = async () => {
      try {
        setLoading(true)
        const response = await api.get('/meters')
        setMeters(response.data)
        setLoading(false)
      } catch (error) {
        setError(error)
      }
    }
    fetchMeters()
    }, []
  )

  if (loading) return <div>Loading...</div>
  if (error) return <div>{error.message}</div>

  return (
    <div>
      <h1 className='font-bold text-2xl'>Workers</h1>
      <hr />
      <div className='grid grid-cols-4 gap-4'>
        {meters.map((meter, index) => (
          <div key={index} className="max-w-sm rounded overflow-hidden shadow-lg">
            <div className="px-6 py-4">
              <div className="font-bold text-xl mb-2">{meter.meter_number}</div>
              <p className="text-gray-700 text-base">
                {meter.meter_status}
              </p>
            </div>
            <div className="px-6 pt-4 pb-2">
              <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">{meter.meter_number}</span>
              <span className="inline-block bg-green-400 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">{meter.meter_status}</span>
              <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#{meter.meter_type}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
