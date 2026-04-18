import './globals.css';
import Link from 'next/link';

const navLinks = [
  { href: '/pricing', label: 'Pricing' },
  { href: '/dashboard', label: 'Dashboard' },
  { href: '/billing', label: 'Billing' },
  { href: '/login', label: 'Login' },
];

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-zinc-950 text-zinc-100">
        <div className="mx-auto flex min-h-screen w-full max-w-7xl flex-col px-4 sm:px-6 lg:px-8">
          <header className="sticky top-0 z-10 mt-4 flex items-center justify-between rounded-2xl border border-zinc-800/80 bg-zinc-950/80 px-4 py-3 backdrop-blur">
            <Link href="/" className="text-lg font-black tracking-tight">
              OpusClip-Style Studio
            </Link>
            <nav className="flex flex-wrap items-center gap-1 text-sm text-zinc-300 sm:gap-2">
              {navLinks.map((item) => (
                <Link
                  key={item.href}
                  href={item.href}
                  className="rounded-lg px-3 py-1.5 transition hover:bg-zinc-800 hover:text-white"
                >
                  {item.label}
                </Link>
              ))}
              <Link
                href="/register"
                className="ml-1 rounded-lg bg-indigo-500 px-3 py-1.5 font-medium text-white transition hover:bg-indigo-400"
              >
                Start Free
              </Link>
            </nav>
          </header>
          <main className="flex-1 py-8">{children}</main>
        </div>
      </body>
    </html>
  );
}
