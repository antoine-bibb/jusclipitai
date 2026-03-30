import './globals.css';
import Link from 'next/link';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <header className="border-b border-zinc-800 px-6 py-4 flex justify-between">
          <Link href="/" className="font-bold">Jus Clip It</Link>
          <nav className="flex gap-4 text-sm">
            <Link href="/pricing">Pricing</Link>
            <Link href="/login">Login</Link>
            <Link href="/dashboard">Dashboard</Link>
          </nav>
        </header>
        <main className="max-w-6xl mx-auto p-6">{children}</main>
      </body>
    </html>
  );
}
