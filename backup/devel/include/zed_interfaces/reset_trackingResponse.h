// Generated by gencpp from file zed_interfaces/reset_trackingResponse.msg
// DO NOT EDIT!


#ifndef ZED_INTERFACES_MESSAGE_RESET_TRACKINGRESPONSE_H
#define ZED_INTERFACES_MESSAGE_RESET_TRACKINGRESPONSE_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace zed_interfaces
{
template <class ContainerAllocator>
struct reset_trackingResponse_
{
  typedef reset_trackingResponse_<ContainerAllocator> Type;

  reset_trackingResponse_()
    : reset_done(false)  {
    }
  reset_trackingResponse_(const ContainerAllocator& _alloc)
    : reset_done(false)  {
  (void)_alloc;
    }



   typedef uint8_t _reset_done_type;
  _reset_done_type reset_done;





  typedef boost::shared_ptr< ::zed_interfaces::reset_trackingResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::zed_interfaces::reset_trackingResponse_<ContainerAllocator> const> ConstPtr;

}; // struct reset_trackingResponse_

typedef ::zed_interfaces::reset_trackingResponse_<std::allocator<void> > reset_trackingResponse;

typedef boost::shared_ptr< ::zed_interfaces::reset_trackingResponse > reset_trackingResponsePtr;
typedef boost::shared_ptr< ::zed_interfaces::reset_trackingResponse const> reset_trackingResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::zed_interfaces::reset_trackingResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::zed_interfaces::reset_trackingResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::zed_interfaces::reset_trackingResponse_<ContainerAllocator1> & lhs, const ::zed_interfaces::reset_trackingResponse_<ContainerAllocator2> & rhs)
{
  return lhs.reset_done == rhs.reset_done;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::zed_interfaces::reset_trackingResponse_<ContainerAllocator1> & lhs, const ::zed_interfaces::reset_trackingResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace zed_interfaces

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::zed_interfaces::reset_trackingResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::zed_interfaces::reset_trackingResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::zed_interfaces::reset_trackingResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::zed_interfaces::reset_trackingResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::zed_interfaces::reset_trackingResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::zed_interfaces::reset_trackingResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::zed_interfaces::reset_trackingResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "e1e87fc9e9e6c154eca93b9fa292cc05";
  }

  static const char* value(const ::zed_interfaces::reset_trackingResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xe1e87fc9e9e6c154ULL;
  static const uint64_t static_value2 = 0xeca93b9fa292cc05ULL;
};

template<class ContainerAllocator>
struct DataType< ::zed_interfaces::reset_trackingResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "zed_interfaces/reset_trackingResponse";
  }

  static const char* value(const ::zed_interfaces::reset_trackingResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::zed_interfaces::reset_trackingResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool reset_done\n"
;
  }

  static const char* value(const ::zed_interfaces::reset_trackingResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::zed_interfaces::reset_trackingResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.reset_done);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct reset_trackingResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::zed_interfaces::reset_trackingResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::zed_interfaces::reset_trackingResponse_<ContainerAllocator>& v)
  {
    s << indent << "reset_done: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.reset_done);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ZED_INTERFACES_MESSAGE_RESET_TRACKINGRESPONSE_H
