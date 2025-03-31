'use client'
import useSWR from 'swr'
import axios from 'axios'

export default function Notifications() {
  const { data } = useSWR('/api/notifications', url => axios.get(url).then(res => res.data))

  return (
    <main className="p-6">
      <h1 className="text-xl font-bold mb-4">Notificações</h1>
      <ul className="list-disc pl-5">
        {data?.map((n: any) => <li key={n.id}>{n.message}</li>)}
      </ul>
    </main>
  )
}