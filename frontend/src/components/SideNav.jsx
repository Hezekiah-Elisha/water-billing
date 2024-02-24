import React from 'react'
import {  Link, NavLink } from 'react-router-dom'
import { 
    UserCircleIcon, AdjustmentsHorizontalIcon,
    Bars3CenterLeftIcon, UsersIcon,
    WrenchIcon, BanknotesIcon,
    CogIcon, DocumentMagnifyingGlassIcon,
    CubeTransparentIcon, BellIcon,
    MapPinIcon,
} from '@heroicons/react/24/solid'

export default function SideNav() {
    // const navigate = useNavigate()
    // const handleSignout = () => {
    //     localStorage.removeItem('token')
    //     navigate('/signin')
    // }
  return (
    <main className="sticky top-0 w-64 bg-blue-500 h-screen p-4 flex flex-col justify-between">
            <div className=''>
                <NavLink to='/dashboard' 
                    className='flex gap-4 align-middle p-4 text-white hover:bg-blue-400 hover:rounded-xl active:bg-blue-400'
                    activeclassname='bg-white'>
                    <Bars3CenterLeftIcon className="h-5 w-5 text-white" />
                    Dashboard
                </NavLink>
                <NavLink to='/dashboard/zones'>
                    <div className='flex gap-4 align-middle p-4 text-white hover:bg-blue-400 hover:rounded-xl'>
                        <MapPinIcon className="h-5 w-5 text-white"/>
                        Zones
                    </div>
                </NavLink>
                {/* <NavLink to='/dashboard/supervisors' 
                    className='flex gap-4 align-middle p-4 text-white hover:bg-blue-400 hover:rounded-xl'
                    activeclassname='bg-white'>
                    <UsersIcon className="h-5 w-5 text-white"/>
                    Supervisors
                </NavLink> */}
                <NavLink to='/dashboard/workers' 
                    className='flex gap-4 align-middle p-4 text-white hover:bg-blue-400 hover:rounded-xl'
                    activeclassname='bg-white'>
                    <WrenchIcon className="h-5 w-5 text-white"/>
                    Workers
                </NavLink>
                <NavLink to='/dashboard/bills' 
                    className='flex gap-4 align-middle p-4 text-white hover:bg-blue-400 hover:rounded-xl'
                    activeclassname='bg-white'>
                    <BanknotesIcon className="h-5 w-5 text-white"/>
                    Bills
                </NavLink>
                <NavLink to='/dashboard/meters' 
                    className='flex gap-4 align-middle p-4 text-white hover:bg-blue-400 hover:rounded-xl'
                    activeClassName='bg-white'>
                    <CogIcon className="h-5 w-5 text-white"/>
                    Meters
                </NavLink>
                <NavLink to='/dashboard/meter-readings' 
                    className='flex gap-4 align-middle p-4 text-white hover:bg-blue-400 hover:rounded-xl'
                    activeclassname='bg-white'>
                    <DocumentMagnifyingGlassIcon className="h-5 w-5 text-white"/>
                    Meter Readings
                </NavLink>
                <NavLink to='/dashboard/customers' 
                    className='flex gap-4 align-middle p-4 text-white hover:bg-blue-400 hover:rounded-xl'
                    activeclassname='bg-white'>
                    <CubeTransparentIcon className="h-5 w-5 text-white"/>
                    Customers
                </NavLink>
            </div>
            <div>
                <Link to='/dashboard/profile' className='flex gap-4 align-middle p-4 text-white hover:bg-blue-400 hover:rounded-xl'>
                    <UserCircleIcon className="h-5 w-5 text-white"/>
                    Profile
                </Link>
                {/* <Link to='/dashboard/settings' className='flex gap-4 align-middle p-4 text-white hover:bg-blue-400 hover:rounded-xl'>
                    <AdjustmentsHorizontalIcon className="h-5 w-5 text-white"/>
                    Settings
                </Link> */}
            </div>
        </main>
  )
}
