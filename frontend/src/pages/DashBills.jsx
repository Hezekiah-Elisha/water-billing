import { useState, useEffect } from 'react'
import api from '../api'

export default function DashBills() {
  const [bills, setBills] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  useEffect(() => {
    const fetchBills = async () => {
      try {
        setLoading(true)
        const response = await api.get('/bills')
        setBills(response.data)
        setLoading(false)
      } catch (error) {
        setError(error)
      }
    }
    fetchBills()
    }, []
  )

  if (loading) return <div>Loading...</div>
  if (error) return <div>{error.message}</div>
  console.log(bills)

  return (
    <div>
      <h1 className='font-bold text-2xl'>Bills</h1>
      <hr />
      <div className='grid grid-cols-4 gap-4'>
        {bills.map((bill, index) => (
          <div key={index} className="max-w-sm rounded overflow-hidden shadow-lg">
            <div className="px-6 py-4">
              <div className="font-bold text-xl mb-2">{bill.meter_id}</div>
              <p className="text-gray-700 text-base">
                {bill.units}
              </p>
              <p className="text-gray-700 text-base">
                {bill.amount}
              </p>
            </div>
            <div className="px-6 pt-4 pb-2">
              <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">{bill.created_at}</span>
              <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">{bill.status}</span>
              {/* <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#{bill.bill_type}</span> */}
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
