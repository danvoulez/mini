'use client'
import { useParams } from 'next/navigation'
import useSWR from 'swr'
import axios from 'axios'

export default function DeliveryInfo() {
  const { id } = useParams()
  const { data } = useSWR(`/api/orders/${id}/delivery`, url => axios.get(url).then(res => res.data))

  return (
    <main className="p-6">
      <h1 className="text-xl font-bold mb-4">Entrega do Pedido #{id}</h1>
      <p>Status: {data?.status}</p>
      <p>Localização: {data?.location}</p>
    </main>
  )
}