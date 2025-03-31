'use client'
import useSWR from 'swr'
import axios from 'axios'

export default function Units() {
  const { data } = useSWR('/api/units', url => axios.get(url).then(res => res.data))

  return (
    <main className="p-6">
      <h1 className="text-xl font-bold mb-4">Unidades de Medida</h1>
      <div>{data?.join(', ')}</div>
    </main>
  )
}