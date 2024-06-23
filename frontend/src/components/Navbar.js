import React from 'react';
import styled from 'styled-components';
import { MdMenu, MdShoppingCart, MdPerson } from 'react-icons/md';
import { Link,useNavigate } from 'react-router-dom';
import { useSidebarContext } from '../context/sidebar_context';
import { useCartContext } from '../context/cart_context';
import { useAuthContext } from '../context/authe_context';

const Navbar = () => {
  const navigate = useNavigate(); // Use useNavigate for programmatic navigation
  const { total_items } = useCartContext();
  const { openSidebar } = useSidebarContext();
  const { isAuthenticated, user, logout } = useAuthContext();

  const handleLogout = () => {
    logout();
    navigate('/');
  };

  return (
    <NavbarWrapper className='bg-white flex'>
      <div className='container w-100'>
        <div className='brand-and-toggler flex flex-between w-100'>
          <Link to='/' className='navbar-brand text-uppercase ls-1 fw-8'>
            <span>INE</span>Study
          </Link>

          <div className='navbar-btns flex'>
            <Link to='/cart' className='cart-btn'>
              <MdShoppingCart />
              <span className='item-count-badge'>{total_items}</span>
            </Link>
            {isAuthenticated ? (
              <>
                <Link to='/profile' className='profile-btn'>
                  <MdPerson />
                </Link>
                <button
                  type='button'
                  className='logout-btn'
                  onClick={handleLogout}
                >
                  Logout
                </button>
              </>
            ) : (
              <Link to='/login' className='login-btn'>
                Login
              </Link>
            )}
            <button
              type='button'
              className='sidebar-open-btn'
              onClick={() => openSidebar()}
            >
              <MdMenu />
            </button>
          </div>
        </div>
      </div>
    </NavbarWrapper>
  );
};

const NavbarWrapper = styled.nav`
  height: 80px;
  box-shadow: rgba(50, 50, 93, 0.15) 0px 16px 12px -2px,
    rgba(0, 0, 0, 0.2) 0px 3px 7px -3px;

  .navbar-brand {
    font-size: 23px;
    span {
      color: var(--clr-orange);
    }
  }
  .cart-btn {
    margin-right: 18px;
    font-size: 23px;
    position: relative;
    .item-count-badge {
      background-color: var(--clr-orange);
      position: absolute;
      right: -10px;
      top: -10px;
      font-size: 12px;
      font-weight: 700;
      display: block;
      width: 23px;
      height: 23px;
      color: var(--clr-white);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
    }
  }

  .login-btn,
  .profile-btn,
  .logout-btn {
    margin-right: 18px;
    font-size: 16px;
    font-weight: 700;
    color: var(--clr-black);
    text-transform: uppercase;
    &:hover {
      color: var(--clr-orange);
    }
  }

  .sidebar-open-btn {
    transition: all 300ms ease-in-out;
    &:hover {
      opacity: 0.7;
    }
  }
`;

export default Navbar;
