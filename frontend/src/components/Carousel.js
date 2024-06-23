import React from 'react';
import styled from 'styled-components';
import Slider from 'react-slick';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';
import { Link } from 'react-router-dom';

const Carousel = ({ courses }) => {
  const settings = {
    dots: false,
    infinite: true,
    speed: 500,
    slidesToShow: 3,
    slidesToScroll: 1,
    autoplay: true,         // Enable autoplay
    autoplaySpeed: 3000,    // Set autoplay speed to 3 seconds
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1,
          infinite: true,
          dots: false,
        },
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          infinite: true,
          dots: false,
        },
      },
    ],
    swipeToSlide: true,
  };

  return (
    <CarouselWrapper>
      <Slider {...settings}>
        {courses.map((course) => (
          <CourseCard key={course.id}>
            <Link to={`/courses/${course.id}`}>
              <img src={course.image} alt={course.title} />
              <div className="course-info">
                <h3>{course.title}</h3>
                <p>{course.description}</p>
                <span>{course.instructor}</span>
              </div>
            </Link>
          </CourseCard>
        ))}
      </Slider>
    </CarouselWrapper>
  );
};

const CarouselWrapper = styled.div`
  .slick-prev,
  .slick-next {
    display: none !important; // Hide the default arrows
  }

  .custom-arrow {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    z-index: 1;
    font-size: 2rem;
    color: var(--clr-orange);
    background: transparent;
    border: none;
    cursor: pointer;
    transition: color 0.3s;
    &:hover {
      color: var(--clr-dark);
    }
  }

  .custom-prev {
    left: 1rem;
  }

  .custom-next {
    right: 1rem;
  }
`;

const CourseCard = styled.div`
  padding: 1rem;
  img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 8px;
    margin-bottom: 1rem;
  }
  .course-info {
    h3 {
      font-size: 1.6rem;
      margin-bottom: 0.5rem;
    }
    p {
      font-size: 1.4rem;
      color: var(--clr-dark);
      margin-bottom: 0.5rem;
    }
    span {
      font-size: 1.2rem;
      color: var(--clr-gray);
    }
  }
`;

export default Carousel;
